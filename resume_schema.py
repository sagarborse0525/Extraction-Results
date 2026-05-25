from pydantic import BaseModel, Field, EmailStr

# -------------------------------
# Structured Output Schema
# -------------------------------
class Experience(BaseModel):
    company: str = Field(description="Company name")
    role: str = Field(description="Job title or role")
    start_date: str = Field(description="Start date in 'Mon YYYY' format, e.g. 'Apr 2023'")
    end_date: str = Field(description="End date in 'Mon YYYY' format, or 'Present' if currently working")
    duration: str = Field(description="Full duration string, e.g. 'Apr 2023 - Present' or 'Jan 2021 - Mar 2023'")
    description: str | None = Field(description="Job responsibilities or achievements", default=None)

class ResumeParser(BaseModel):
    name: str = Field(description="The name of the candidate")
    email: EmailStr = Field(description="Email address")
    phone: str | None = Field(description="Phone number", default=None)
    skills: list[str] = Field(description="List of skills")
    experience: list[Experience] = Field(description="List of work experience")
    certifications: list[str] | None = Field(description="List of certifications", default=None)
    address: str | None = Field(description="Address of the candidate", default=None)
    linkedin: str | None = Field(description="LinkedIn URL", default=None)