
import pytest
from sqlalchemy import text
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.repositories.users_repository import UsersRepository

db_connection = DBConnectionHandler()
connection = db_connection.get_engine().connect()
@pytest.mark.skip(reason="Sensitive test")
def test_insert_user():
    mocked_name = "Junior"
    mocked_phone = "11999999999"
    mocked_cpf = "11111111111"
    mocked_email = "a@a.com"
    mocked_password = "123456"

    users_repository = UsersRepository()
    users_repository.insert_user(mocked_name, mocked_phone, mocked_cpf, mocked_email, mocked_password)

    sql = '''
        SELECT * FROM users 
        WHERE name = '{}' 
        AND phone = '{}' 
        AND cpf = '{}' 
        AND email = '{}'  
        AND password = '{}'  
    '''.format(mocked_name, mocked_phone, mocked_cpf, mocked_email, mocked_password)

    response = connection.execute(text(sql))
    registry = response.fetchall()[0]

    assert registry.name == mocked_name
    assert registry.phone == mocked_phone
    assert registry.cpf == mocked_cpf
    assert registry.email == mocked_email
    assert registry.password == mocked_password

    connection.execute(text(f'DELETE FROM users WHERE id = {registry.id}'))
    connection.commit()

@pytest.mark.skip(reason="Sensitive test")
def test_select_user():
    mocked_id = 555
    mocked_name = "Junior2"
    mocked_phone = "119999"
    mocked_cpf = "11111111"
    mocked_email = "e@a.com"
    mocked_password = "3456"

    users_repository = UsersRepository()

    sql = '''
        INSERT INTO users 
        (id,name, phone, cpf, email, password) 
        VALUES ('{}', '{}', '{}', '{}', '{}', '{}')
    '''.format(mocked_id,mocked_name, mocked_phone, mocked_cpf, mocked_email, mocked_password)
    connection.execute(text(sql))
    connection.commit()

    response = users_repository.select_user(mocked_id)

    assert response[0].name == mocked_name
    assert response[0].phone == mocked_phone
    assert response[0].cpf == mocked_cpf
    assert response[0].email == mocked_email
    assert response[0].password == mocked_password

    connection.execute(text(f'DELETE FROM users WHERE id = {response[0].id}'))
    connection.commit()
