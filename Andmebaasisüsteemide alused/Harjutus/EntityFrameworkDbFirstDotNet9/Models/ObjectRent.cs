using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class ObjectRent
{
    public int Id { get; set; }

    public int EmployeeId { get; set; }

    public int DeviceId { get; set; }

    public DateTime StartDate { get; set; }

    public DateTime EndDate { get; set; }

    public virtual Device Device { get; set; } = null!;

    public virtual Employee Employee { get; set; } = null!;
}
