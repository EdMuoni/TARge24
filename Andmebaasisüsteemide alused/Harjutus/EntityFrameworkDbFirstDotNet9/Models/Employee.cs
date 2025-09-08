using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Employee
{
    public int Id { get; set; }

    public string? FirstName { get; set; }

    public string? LastName { get; set; }

    public string? Phone { get; set; }

    public string? Email { get; set; }

    public string? PersonalCode { get; set; }

    public int? AddressId { get; set; }

    public virtual Address? Address { get; set; }

    public virtual ICollection<Child> Children { get; set; } = new List<Child>();

    public virtual ICollection<HealthCheck> HealthChecks { get; set; } = new List<HealthCheck>();

    public virtual ICollection<Hint> Hints { get; set; } = new List<Hint>();

    public virtual ICollection<JobHistory> JobHistories { get; set; } = new List<JobHistory>();

    public virtual ICollection<ObjectRent> ObjectRents { get; set; } = new List<ObjectRent>();

    public virtual ICollection<Request> Requests { get; set; } = new List<Request>();

    public virtual ICollection<Salary> Salaries { get; set; } = new List<Salary>();

    public virtual ICollection<Sickleaf> Sickleaves { get; set; } = new List<Sickleaf>();

    public virtual ICollection<VacationList> VacationLists { get; set; } = new List<VacationList>();
}
