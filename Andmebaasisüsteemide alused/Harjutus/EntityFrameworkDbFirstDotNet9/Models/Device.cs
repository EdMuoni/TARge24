using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Device
{
    public int Id { get; set; }

    public string Manufacturer { get; set; } = null!;

    public string Name { get; set; } = null!;

    public string Type { get; set; } = null!;

    public string SerialNumber { get; set; } = null!;

    public string Condition { get; set; } = null!;

    public virtual ICollection<ObjectRent> ObjectRents { get; set; } = new List<ObjectRent>();
}
