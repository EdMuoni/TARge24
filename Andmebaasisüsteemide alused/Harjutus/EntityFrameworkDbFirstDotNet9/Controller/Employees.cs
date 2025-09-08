using EntityFrameworkDbFirstDotNet9.Models;
using Microsoft.AspNetCore.Http;
using Microsoft.AspNetCore.Mvc;

namespace EntityFrameworkDbFirstDotNet9.Controller
{
    [Route("api/[controller]")]
    [ApiController]
    public class Employees(DatabaseTaskDbContext context) : ControllerBase
    {
        public async Task<IActionResult> Get()
        {
            var employees = await context.Employees.ToListAsync();
            return Ok(employees);
        }
    }
}
