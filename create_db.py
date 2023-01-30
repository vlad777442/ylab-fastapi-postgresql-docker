from app.db.database import Base, engine


print("Creating database...")

Base.metadata.create_all(engine)
