namespace NSUDA.Handler
{
    /// <summary>
    /// Provides request handlers.
    /// </summary>
    internal static partial class Handler 
    {
        [HandlerPath("/")]
        internal async static Task HandleIndex(HttpContext requestContext)
        {   
            requestContext.Response.ContentType = "text/html; charset=utf-8";
            await requestContext.Response.SendFileAsync("wwwroot/index.html");
        }
    }
}