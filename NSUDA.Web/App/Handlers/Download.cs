namespace NSUDA.Handler
{
    /// <summary>
    /// Provides request handlers.
    /// </summary>
    internal static partial class Handler 
    {
        [HandlerPath("/downloads")]
        internal async static Task HandleDownload(HttpContext requestContext)
        {   
            requestContext.Response.ContentType = "text/html; charset=utf-8";
            await requestContext.Response.SendFileAsync("wwwroot/download.html");
        }
    }
}