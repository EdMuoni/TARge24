using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class VacationList
{
    public int Id { get; set; }

    public int EmployeeId { get; set; }

    public DateTime StartDate { get; set; }

    public DateTime EndDate { get; set; }

    public DateTime DateApproved { get; set; }

    public int TotalDays { get; set; }

    public int VacationDaysUsed { get; set; }

    public int VacationDaysReamining { get; set; }

    public virtual Employee Employee { get; set; } = null!;
}
