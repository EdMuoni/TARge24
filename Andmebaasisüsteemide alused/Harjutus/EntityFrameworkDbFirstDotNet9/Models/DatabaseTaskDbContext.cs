using System;
using System.Collections.Generic;
using Microsoft.EntityFrameworkCore;

namespace EntityFrameworkDbFirstDotNet9.Models;

public class DatabaseTaskDbContext : DbContext
{
    public DatabaseTaskDbContext()
    {
    }

    public DatabaseTaskDbContext(DbContextOptions<DatabaseTaskDbContext> options)
        : base(options)
    {
    }

    public virtual DbSet<Access> Accesses { get; set; }

    public virtual DbSet<Address> Addresses { get; set; }

    public virtual DbSet<Child> Children { get; set; }

    public virtual DbSet<Device> Devices { get; set; }

    public virtual DbSet<Employee> Employees { get; set; }

    public virtual DbSet<HealthCheck> HealthChecks { get; set; }

    public virtual DbSet<Hint> Hints { get; set; }

    public virtual DbSet<JobHistory> JobHistories { get; set; }

    public virtual DbSet<ObjectRent> ObjectRents { get; set; }

    public virtual DbSet<Position> Positions { get; set; }

    public virtual DbSet<Request> Requests { get; set; }

    public virtual DbSet<Salary> Salaries { get; set; }

    public virtual DbSet<Sickleaf> Sickleaves { get; set; }

    public virtual DbSet<VacationList> VacationLists { get; set; }

    public virtual DbSet<WorkTopic> WorkTopics { get; set; }

    protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
#warning To protect potentially sensitive information in your connection string, you should move it out of source code. You can avoid scaffolding the connection string by using the Name= syntax to read it from configuration - see https://go.microsoft.com/fwlink/?linkid=2131148. For more guidance on storing connection strings, see https://go.microsoft.com/fwlink/?LinkId=723263.
        => optionsBuilder.UseSqlServer("Server=DESKTOP-KMVSVQK;Database=DatabaseTaskDb;Trusted_Connection=True;MultipleActiveResultSets=True;TrustServerCertificate=True;");

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Access>(entity =>
        {
            entity.Property(e => e.Description).HasColumnName("description");
        });

        modelBuilder.Entity<Child>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_Children_EmployeeId");

            entity.Property(e => e.BirthDate).HasColumnName("birthDate");
            entity.Property(e => e.FirstName).HasColumnName("firstName");
            entity.Property(e => e.LastName).HasColumnName("lastName");

            entity.HasOne(d => d.Employee).WithMany(p => p.Children).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<Device>(entity =>
        {
            entity.Property(e => e.Condition).HasColumnName("condition");
            entity.Property(e => e.Manufacturer).HasColumnName("manufacturer");
            entity.Property(e => e.Name).HasColumnName("name");
            entity.Property(e => e.SerialNumber).HasColumnName("serialNumber");
            entity.Property(e => e.Type).HasColumnName("type");
        });

        modelBuilder.Entity<Employee>(entity =>
        {
            entity.HasIndex(e => e.AddressId, "IX_Employees_AddressId");

            entity.HasOne(d => d.Address).WithMany(p => p.Employees).HasForeignKey(d => d.AddressId);
        });

        modelBuilder.Entity<HealthCheck>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_HealthChecks_EmployeeId");

            entity.Property(e => e.IsHealthy).HasColumnName("isHealthy");
            entity.Property(e => e.LastcheckDate).HasColumnName("lastcheckDate");
            entity.Property(e => e.NextcheckDate).HasColumnName("nextcheckDate");

            entity.HasOne(d => d.Employee).WithMany(p => p.HealthChecks).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<Hint>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_Hints_EmployeeId");

            entity.HasIndex(e => e.WorkTopicId, "IX_Hints_WorkTopicId");

            entity.Property(e => e.CreatedDate).HasColumnName("createdDate");
            entity.Property(e => e.Description).HasColumnName("description");
            entity.Property(e => e.ReviewedDate).HasColumnName("reviewedDate");

            entity.HasOne(d => d.Employee).WithMany(p => p.Hints).HasForeignKey(d => d.EmployeeId);

            entity.HasOne(d => d.WorkTopic).WithMany(p => p.Hints).HasForeignKey(d => d.WorkTopicId);
        });

        modelBuilder.Entity<JobHistory>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_JobHistories_EmployeeId");

            entity.HasIndex(e => e.PositionId, "IX_JobHistories_PositionId");

            entity.Property(e => e.EndDate).HasColumnName("endDate");
            entity.Property(e => e.StartDate).HasColumnName("startDate");

            entity.HasOne(d => d.Employee).WithMany(p => p.JobHistories).HasForeignKey(d => d.EmployeeId);

            entity.HasOne(d => d.Position).WithMany(p => p.JobHistories).HasForeignKey(d => d.PositionId);
        });

        modelBuilder.Entity<ObjectRent>(entity =>
        {
            entity.HasIndex(e => e.DeviceId, "IX_ObjectRents_DeviceId");

            entity.HasIndex(e => e.EmployeeId, "IX_ObjectRents_EmployeeId");

            entity.Property(e => e.EndDate).HasColumnName("endDate");
            entity.Property(e => e.StartDate).HasColumnName("startDate");

            entity.HasOne(d => d.Device).WithMany(p => p.ObjectRents).HasForeignKey(d => d.DeviceId);

            entity.HasOne(d => d.Employee).WithMany(p => p.ObjectRents).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<Position>(entity =>
        {
            entity.HasIndex(e => e.AccessId, "IX_Positions_AccessId");

            entity.Property(e => e.PositionCreatedDate).HasColumnName("positionCreatedDate");
            entity.Property(e => e.PositionDisabledDate).HasColumnName("positionDisabledDate");

            entity.HasOne(d => d.Access).WithMany(p => p.Positions).HasForeignKey(d => d.AccessId);
        });

        modelBuilder.Entity<Request>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_Requests_EmployeeId");

            entity.HasIndex(e => e.WorkTopicId, "IX_Requests_workTopicId");

            entity.Property(e => e.CreatedDate).HasColumnName("createdDate");
            entity.Property(e => e.Description).HasColumnName("description");
            entity.Property(e => e.ReviewedDate).HasColumnName("reviewedDate");
            entity.Property(e => e.Status).HasColumnName("status");
            entity.Property(e => e.WorkTopicId).HasColumnName("workTopicId");

            entity.HasOne(d => d.Employee).WithMany(p => p.Requests).HasForeignKey(d => d.EmployeeId);

            entity.HasOne(d => d.WorkTopic).WithMany(p => p.Requests).HasForeignKey(d => d.WorkTopicId);
        });

        modelBuilder.Entity<Salary>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_Salaries_EmployeeId");

            entity.Property(e => e.SalaryAmount).HasColumnName("salaryAmount");

            entity.HasOne(d => d.Employee).WithMany(p => p.Salaries).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<Sickleaf>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_Sickleaves_EmployeeId");

            entity.Property(e => e.EndDate).HasColumnName("endDate");
            entity.Property(e => e.IsActive).HasColumnName("isActive");
            entity.Property(e => e.StartDate).HasColumnName("startDate");

            entity.HasOne(d => d.Employee).WithMany(p => p.Sickleaves).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<VacationList>(entity =>
        {
            entity.HasIndex(e => e.EmployeeId, "IX_VacationLists_EmployeeId");

            entity.Property(e => e.DateApproved).HasColumnName("dateApproved");
            entity.Property(e => e.EndDate).HasColumnName("endDate");
            entity.Property(e => e.StartDate).HasColumnName("startDate");
            entity.Property(e => e.TotalDays).HasColumnName("totalDays");
            entity.Property(e => e.VacationDaysReamining).HasColumnName("vacationDaysReamining");
            entity.Property(e => e.VacationDaysUsed).HasColumnName("vacationDaysUsed");

            entity.HasOne(d => d.Employee).WithMany(p => p.VacationLists).HasForeignKey(d => d.EmployeeId);
        });

        modelBuilder.Entity<WorkTopic>(entity =>
        {
            entity.Property(e => e.Description).HasColumnName("description");
        });

        OnModelCreatingPartial(modelBuilder);
    }

    partial void OnModelCreatingPartial(ModelBuilder modelBuilder);
}
