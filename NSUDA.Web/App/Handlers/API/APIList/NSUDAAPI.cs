namespace NSUDA.API
{
    /// <summary>
    /// Provides api handlers for NSUDA app.
    /// </summary>
    internal class NSUDAAPI : IAPI
    {
        async Task IAPI.HandleRequest(HttpContext context)
        {
            context.Request.Path.
                StartsWithSegments("/api/NSUDA", out PathString requestName);
            if (requestName == "/GetConfig" && context.Request.Method == "GET")
            {
                await GetConfig(context);
            }
            else
            {
                await context.Response.WriteAsync("Hello, NSUDA!");
            }
        }

        private async Task GetConfig(HttpContext context)
        {
            await context.Response.WriteAsync("Hello, NSUDA!");
        }
    }
}