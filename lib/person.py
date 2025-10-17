#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name=None, job=None):
        self._name = None
        self._job = None
        if name is not None:
            self.name = name  # ✅ uses setter for validation and title case
        if job is not None:
            self.job = job    # ✅ uses setter for validation

    # ----- name property -----
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (1 <= len(value) <= 25):
            self._name = value.title()  # convert to title case
        else:
            print("Name must be string between 1 and 25 characters.")

    # ----- job property -----
    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
