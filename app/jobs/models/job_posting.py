from datetime import datetime
import re

class JobPosting:
    def __init__(self, company:str, role:str, date_applied:str, source:str, status:str, notes:str):
        """
        Required args -> company, role, date_applied 
        """
        self.company = company.strip()
        self.role = role.strip()
        self.date_applied = date_applied
        self.source = source.strip()
        self.status = status.strip()
        self.notes = notes.strip()

        if not self.is_valid():
            raise ValueError("Invalid JobPosting data")

    def is_valid(self) -> bool:
        return self.is_valid_date(self.date_applied) and self.is_valid_company(self.company)

    @staticmethod
    def is_valid_date(date_str) -> bool:
        """
        Method designed to check the validity of a date.
        """
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return True
        except ValueError:
            return False

    @staticmethod
    def is_valid_company(name) -> bool:
        """
        Method designed to check if user entered a valid company name
        """
        stripped = name.strip()
        return bool(len(stripped) > 0 and re.match(r"^[A-Za-z0-9&.\- ]{2,}$", stripped))
