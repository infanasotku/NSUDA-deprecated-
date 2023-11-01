namespace NSUDA.API
{
    internal static class APIExtensions
    {
        internal static IApplicationBuilder UseAPI(this IApplicationBuilder builder)
        {
            return builder.UseMiddleware<API>();
        }
    }

    internal class API
    {
        private readonly RequestDelegate _next;
        internal API(RequestDelegate next)
        {
            _next = next;
        }

        public async Task InvokeAsync(HttpContext context)
        {
            await APIBuilder.Build(context).HandleRequest(context);
        }
    }

}