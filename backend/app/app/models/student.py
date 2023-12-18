from app.db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String, ARRAY

# TODO: create Student model

'''
{
        text: 'Email',
        sortable: true,
        value: 'email',
        align: 'left',
      },
      {
        text: 'Nombre completo',
        sortable: true,
        value: 'full_name',
        align: 'left',
      },
'''

class Student(Base):
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    is_active = Column(Boolean(), default=True)
    email = Column(String, unique=True, index=True, nullable=False)