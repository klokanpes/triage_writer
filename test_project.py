import pytest
import os
import csv
from project import Print_to_pdf, Make_csv, Check_victims_and_print

@pytest.fixture
def create_and_delete_file1():
    # Create files
    with open("victims.csv", "w") as file:
        writer = csv.DictWriter(
                file, fieldnames=["id", "date", "time", "colour"]
            )
        writer.writeheader()
    Print_to_pdf(123, 0)
    yield

    # delete files
    if os.path.isfile("victims.csv"):
        os.remove("victims.csv")
    if os.path.isfile("Triage report from .pdf"):
        os.remove("Triage report from .pdf")
def test_Print_to_pdf(create_and_delete_file1):

    assert os.path.isfile("Triage report from .pdf")


@pytest.fixture
def create_and_delete_file2():
    # Create file
    Make_csv(1, "2024-07-24", "10:00:00", "Green")
    yield

    # remove file
    if os.path.isfile("victims.csv"):
        os.remove("victims.csv")
def test_Make_csv(create_and_delete_file2):
    assert os.path.isfile("victims.csv")

@pytest.fixture
def create_and_delete_file3():
    with open("victims.csv", "w") as file:
        file.write("1, 2, 3, 4")
    yield
def test_Check_victims_and_print(create_and_delete_file3):
    Check_victims_and_print(123,0)
    assert not os.path.isfile("victims.csv")

