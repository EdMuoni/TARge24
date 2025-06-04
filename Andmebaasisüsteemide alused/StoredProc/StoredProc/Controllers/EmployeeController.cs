using Microsoft.AspNetCore.Mvc;
using Microsoft.Data.SqlClient;
using Microsoft.EntityFrameworkCore;
using Microsoft.EntityFrameworkCore.Metadata.Internal;
using StoredProc.Data;
using StoredProc.Models;

namespace StoredProc.Controllers
{
    public class EmployeeController : Controller
    {
        private StoredProcDbContext _context;

        public IConfiguration _config { get; }

        public EmployeeController
        (
            StoredProcDbContext context,
            IConfiguration config
        )
        {
            _context = context;
            _config = config;
        }

        public IActionResult Index()
        {
            return View();
        }

        //teha sp andmebaasi, mis annab andmed töötajate kohta
        public IEnumerable<Employee> SearchResult()
        {
            var result = _context.Employees
                .FromSqlRaw<Employee>("EXEC spSearchEmployees")
                .ToList();

            return result;
        }

        [HttpGet]
        public IActionResult DynamicSQL()
        {
            string connectionStr = _config.GetConnectionString("DefaultConnection");

            using (SqlConnection con = new SqlConnection(connectionStr))
            {
                SqlCommand cmd = new SqlCommand();
                cmd.Connection = con;
                cmd.CommandText = "dbo.spSearchEmployees";
                cmd.CommandType = System.Data.CommandType.StoredProcedure;
                con.Open();
                SqlDataReader sdr = cmd.ExecuteReader();
                List<Employee> employees = new List<Employee>(); // Corrected type for the collection
                while (sdr.Read())
                {
                    var details = new Employee();
                    details.FirstName = sdr["FirstName"].ToString();
                    details.LastName = sdr["LastName"].ToString();
                    details.Gender = sdr["Gender"].ToString();
                    details.Salary = Convert.ToInt32(sdr["Salary"]);
                    employees.Add(details); // Use the correct collection
                }
                return View(employees); // Pass the correct collection to the view
            }
        }
    }
