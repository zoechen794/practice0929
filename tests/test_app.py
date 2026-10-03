import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_status_code(client):
    """測試首頁 HTTP 狀態碼是否為 200"""
    response = client.get('/')
    assert response.status_code == 200

def test_index_content(client):
    """測試首頁內容是否包含歡迎或時間資訊"""
    response = client.get('/')
    html = response.data.decode('utf-8')
    assert "Flask" in html or "首頁" in html or "練習" in html
