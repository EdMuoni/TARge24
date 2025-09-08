using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Salary
{
    public int Id { get; set; }

    public int EmployeeId { get; set; }

    public int SalaryAmount { get; set; }

    public DateTime StartDate { get; set; }

    public virtual Employee Employee { get; set; } = null!;
}
