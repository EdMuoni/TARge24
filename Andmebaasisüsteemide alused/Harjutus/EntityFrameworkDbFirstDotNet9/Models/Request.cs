using System;
using System.Collections.Generic;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class Request
{
    public int Id { get; set; }

    public int WorkTopicId { get; set; }

    public int EmployeeId { get; set; }

    public DateTime CreatedDate { get; set; }

    public DateTime ReviewedDate { get; set; }

    public string? Status { get; set; }

    public string? Description { get; set; }

    public virtual Employee Employee { get; set; } = null!;

    public virtual WorkTopic WorkTopic { get; set; } = null!;
}
