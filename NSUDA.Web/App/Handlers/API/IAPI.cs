
namespace NSUDA.API
{
    internal interface IAPI
    {
        internal Task HandleRequest(HttpContext context);
    }
}