
namespace NSUDA.API
{
    /// <summary>
    /// Expose API handler.
    /// </summary>
    internal interface IAPI
    {
        /// <summary>
        /// Handles the request.
        /// </summary>
        internal Task HandleRequest(HttpContext context);
    }
}