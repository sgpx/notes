using Microsoft.AspNetCore.Mvc;

namespace HelloWorldApp.Controllers
{
    public class HXController : Controller
    {
        public IActionResult Index()
        {
            return Content("HX1");
        }
    }
}