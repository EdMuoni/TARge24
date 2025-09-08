using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class HealthCheck
{
    public int Id { get; set; }

    public int EmployeeId { get; set; }

    public DateTime LastcheckDate { get; set; }

    public DateTime NextcheckDate { get; set; }

    public bool IsHealthy { get; set; }

    public virtual Employee Employee { get; set; } = null!;
}
