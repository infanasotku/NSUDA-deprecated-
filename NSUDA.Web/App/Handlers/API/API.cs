using System.Diagnostics;

namespace NSUDA.API
{
    /// <summary>
    /// Extenstion to registrate from App.
    /// </summary>
    internal static class APIExtensions
    {
        internal static IApplicationBuilder UseAPI(this IApplicationBuilder builder)
        {
            return builder.UseMiddleware<API>();
        }
    }

    /// <summary>
    /// Provides API module who handle the api request.
    /// </summary>
    internal class API
    {
        private readonly RequestDelegate _next;
        public API(RequestDelegate next)
        {
            _next = next;
        }

        /// <summary>
        /// Invokes the required handler for specified <paramref name="context"/>.
        /// </summary>
        public async Task InvokeAsync(HttpContext context)
        {
            try
            {
                IAPI? handler = APIBuilder.Build(context);
                if (handler is not null)
                {
                    await handler.HandleRequest(context);
                }
            }
            catch (Exception ex)
            {
                Debug.WriteLine(ex.Message);
            }
            finally
            {
                if (!context.Response.HasStarted)
                {
                    await _next.Invoke(context);
                }
            }
        }
    }

}