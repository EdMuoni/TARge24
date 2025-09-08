using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class WorkTopic
{
    public int Id { get; set; }

    public string Description { get; set; } = null!;

    public virtual ICollection<Hint> Hints { get; set; } = new List<Hint>();

    public virtual ICollection<Request> Requests { get; set; } = new List<Request>();
}
