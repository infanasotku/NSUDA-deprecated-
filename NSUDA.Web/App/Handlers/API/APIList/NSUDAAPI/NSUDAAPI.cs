namespace NSUDA.API
{
    using Newtonsoft.Json;
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
            string email = context.Request.Query["email"].ToString();
            CreateClientConfig(email);
            await context.Response.WriteAsync("Hello, NSUDA!");
        }

        private string CreateClientConfig(string email)
        {
            string configStr = File.ReadAllText("config/client_config.json");
            dynamic config = JsonConvert.DeserializeObject(configStr)!;
            dynamic outbounds = config.GetType().GetProperty("ChildrenTokens").GetValue(config, null);
            return "";
        }
    }
}