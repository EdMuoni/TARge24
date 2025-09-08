using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Access
{
    public int Id { get; set; }

    public string Description { get; set; } = null!;

    public virtual ICollection<Position> Positions { get; set; } = new List<Position>();
}
