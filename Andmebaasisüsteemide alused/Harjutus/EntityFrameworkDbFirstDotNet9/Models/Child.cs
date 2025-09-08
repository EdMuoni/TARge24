using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Child
{
    public int Id { get; set; }

    public int EmployeeId { get; set; }

    public DateTime BirthDate { get; set; }

    public string FirstName { get; set; } = null!;

    public string LastName { get; set; } = null!;

    public virtual Employee Employee { get; set; } = null!;
}
