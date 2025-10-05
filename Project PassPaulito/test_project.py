import os
import csv
from project import check_database, add_password_manual, add_password_auto

# Test 1: Check if database is created correctly
def test_check_database():
    if os.path.exists("Database.txt"):
        os.remove("Database.txt")

    check_database()
    assert os.path.exists("Database.txt")

    with open("Database.txt", "r") as f:
        header = f.readline().strip()
        assert header == "ID,Website,Username,Password"

# Test 2: Thêm password manual
def test_add_password_manual(monkeypatch):

    inputs = iter(["youtube.com", "paul", "123456"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_password_manual()

    with open("Database.txt", "r") as db:
        lines = list(csv.reader(db))
        assert lines[-1][1] == "youtube.com"
        assert lines[-1][2] == "paul"
        assert lines[-1][3] == "123456"

# Test 3: Tạo password tự động
def test_add_password_auto(monkeypatch):
    inputs = iter(["facebook.com", "minmin2k", "10"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    add_password_auto()

    with open("Database.txt", "r") as db:
        lines = list(csv.reader(db))
        assert lines[-1][1] == "facebook.com"
        assert lines[-1][2] == "minmin2k"
        assert len(lines[-1][3]) == 10
