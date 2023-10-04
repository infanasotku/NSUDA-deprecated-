namespace NSUDA.Handler
{
    /// <summary>
    /// Provides request handlers.
    /// </summary>
    internal static partial class Handler 
    {
        [HandlerPath("/NSUDA")]
        internal async static Task HandleNSUDA(HttpContext requestContext)
        {   
            requestContext.Response.ContentType = "text/html; charset=utf-8";
            await requestContext.Response.SendFileAsync("wwwroot/NSUDA.html");
        }
    }
}