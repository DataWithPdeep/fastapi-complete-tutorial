from fastapi import FastAPI, Depends,HTTPException, Query
from sqlalchemy.orm import Session
from database import engine, SessionLocal
import os
from dotenv import load_dotenv
import model,schemas
from auth import create_token, verify_token
load_dotenv()
#db Dpendency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Login API
model.Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/login")
def login():
     return{
          "access_token":create_token({"user":"admin"}),
          "token_type":"bearer"
     }
#home
@app.get("/")
def home():
    return{
        "message":"Blog APi Start"
    }
#Create Blog Protected
#Create Blog
@app.post("/blogs", response_model=schemas.BlogResponse)
def create_blog(blog:schemas.BlogCreate, db:Session = Depends(get_db), user =Depends(verify_token)):
    new_blog = model.Blog(
        title = blog.title,
        content = blog.content
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

#Read ALL Blog
@app.get("/blogs")
def get_blogs(page: int = 1, 
              limit: int = 5, 
              search:str = Query(default=""),
              db: Session = Depends(get_db)):
    query = db.query(model.Blog)
    if  search:
         query = query.filter(model.Blog.title.ilike(f"%{search}"))

    total = query.count()
    start = (page-1)*limit
    blogs = query.offset(start).limit(limit).all()

    return {
         "page":page,
         "limit": limit,
         "total": total,
         "data":blogs
    }

#Read One Blog
@app.get("/blog/{id}", response_model=schemas.BlogResponse)
def get_blog(id:int, db: Session = Depends(get_db)):
    blog = db.query(model.Blog).filter(model.Blog.id == id).first()

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")
    return blog

#Update Blog API, Protected
@app.put("/blogs/{id}", response_model=schemas.BlogResponse)
def update_blog(id:int,blog:schemas.BlogCreate, db: Session = Depends(get_db), user = Depends(verify_token)):
    existing_blog = db.query(model.Blog).filter(model.Blog.id==id).first()

    if not existing_blog:
            raise HTTPException(status_code=404, detail="Blog not found")
    existing_blog.title = blog.title
    existing_blog.content = blog.content

    db.commit()

    return existing_blog

#delete bLOG api, Protected
@app.delete("/blogs/{id}")
def delete_blog(id:int, db: Session = Depends(get_db), user = Depends(verify_token)):
    blog = db.query(model.Blog).filter(model.Blog.id == id)

    if not blog.first():
            raise HTTPException(status_code=404, detail="Blog not found")
    blog.delete()
    db.commit()

    return{
         "message":"Blog Deleted succesfully"
    }


