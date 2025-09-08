using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Position
{
    public int Id { get; set; }

    public int AccessId { get; set; }

    public DateTime PositionCreatedDate { get; set; }

    public DateTime PositionDisabledDate { get; set; }

    public virtual Access Access { get; set; } = null!;

    public virtual ICollection<JobHistory> JobHistories { get; set; } = new List<JobHistory>();
}
