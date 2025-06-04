-- Loome uue andmebaasi varundamise näite jaoks
CREATE DATABASE MinuAndmebaas;
GO

-- Valikuline: Loome andmebaasi sisse tabeli ja lisame andmed, et varundus poleks tühi
USE MinuAndmebaas;
GO

create TABLE Products (
    ProductsId INT PRIMARY KEY IDENTITY(1,1),
    Name NVARCHAR(50),
    Price int
);

INSERT INTO Products (Name, Price) VALUES ('Laptop', 1200);
INSERT INTO Products (Name, Price) VALUES ('Mouse', 25);
GO

-- Täielik varundamine
BACKUP DATABASE MinuAndmebaas
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\MinuAndmebaas_FullBackup.bak'
WITH NOFORMAT, NOINIT, NAME = 'MinuAndmebaas - Täielik varundamine', SKIP, NOREWIND, NOUNLOAD, STATS = 10;
GO

-- Täielik varundamine enda loodud andmebaasist
BACKUP DATABASE MinuAndmebaas
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\MinuAndmebaas_FullBackup.bak'
WITH NOFORMAT, NOINIT,  
NAME = 'MinuAndmebaas - Täielik varundamine',  
SKIP, NOREWIND, NOUNLOAD, STATS = 10;

-- Täielik varundus kasutades WITH FORMAT, mis loob uue meedia päise
BACKUP DATABASE MinuAndmebaas
TO DISK = 'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\Backup\MinuAndmebaas_FormatBackup.bak'
WITH FORMAT, 
NAME = 'MinuAndmebaas - Formaaditud varundus',
STATS = 10;

-- Andmebaasi taastemudeli muutmine FULL peale
ALTER DATABASE MinuAndmebaas
SET RECOVERY FULL;
GO

-- Kontrollime, kas muudatus õnnestus
SELECT name, recovery_model_desc
FROM sys.databases
WHERE name = 'MinuAndmebaas';