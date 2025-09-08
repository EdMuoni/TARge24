Insert into Employees values ('Mark', 'Hastings', 'Male', 60000)
Insert into Employees values ('Steve', 'Pound', 'Male', 45000)
Insert into Employees values ('Ben', 'Hoskins', 'Male', 70000)
Insert into Employees values ('Philip', 'Hastings', 'Male', 45000)
Insert into Employees values ('Mary', 'Lambeth', 'Female', 30000)
Insert into Employees values ('Valarie', 'Vikings', 'Female', 35000)
Insert into Employees values ('John', 'Stanmore', 'Male', 80000)


create procedure spSearchEmployees
@FirstName nvarchar(100),
@LastName nvarchar(100),
@Gender nvarchar(100),
@Salary int
as
begin

	select * from Employees where
	(FirstName = @FirstName or @FirstName is null) and
	(LastName = @LastName or @LastName is null) and
	(Gender = @Gender or @Gender is null) and
	(Salary = @Salary or @Salary is null)
end
go

alter table Employees
add Id int primary key identity