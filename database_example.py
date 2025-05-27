from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Define the database connection URL (using in-memory SQLite for this example)
DATABASE_URL = "sqlite:///:memory:"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Define a base for declarative models
Base = declarative_base()

# Define a simple model: User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', email='{self.email}')>"

# Create the table in the database (if it doesn't exist)
Base.metadata.create_all(bind=engine)

# Create a SessionLocal class to interact with the database
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def demonstrate_crud():
    """Demonstrates Create, Read, Update, Delete operations."""
    db = SessionLocal()

    print("Demonstrating SQLAlchemy CRUD operations...")

    # Create
    print("\n--- Create ---")
    new_user1 = User(name="Alice Wonderland", email="alice@example.com")
    new_user2 = User(name="Bob The Builder", email="bob@example.com")
    db.add(new_user1)
    db.add(new_user2)
    db.commit()
    db.refresh(new_user1)
    db.refresh(new_user2)
    print(f"Added users: {new_user1}, {new_user2}")

    # Read
    print("\n--- Read ---")
    all_users = db.query(User).all()
    print("All users:")
    for user in all_users:
        print(user)

    alice = db.query(User).filter(User.name == "Alice Wonderland").first()
    print(f"Found Alice: {alice}")

    # Update
    print("\n--- Update ---")
    if alice:
        alice.email = "alice.wonderland@newdomain.com"
        db.commit()
        db.refresh(alice)
        print(f"Updated Alice: {alice}")
    else:
        print("Alice not found for update.")

    # Delete
    print("\n--- Delete ---")
    bob = db.query(User).filter(User.name == "Bob The Builder").first()
    if bob:
        db.delete(bob)
        db.commit()
        print(f"Deleted Bob. Remaining users:")
        remaining_users = db.query(User).all()
        for user in remaining_users:
            print(user)
        if not remaining_users:
            print("No users remaining.")
    else:
        print("Bob not found for deletion.")

    db.close()

if __name__ == "__main__":
    demonstrate_crud()
