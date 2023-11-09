namespace NSUDA.API
{
    /// <summary>
    /// Provides builder for API handlers.
    /// </summary>
    internal static class APIBuilder
    {
        /// <summary>
        /// Builds and returns the API handler by
        /// provided <paramref name="context"/>.
        /// </summary>
        internal static IAPI? Build(HttpContext context)
        {
            if (context.Request.Path.
                StartsWithSegments("/api", out PathString remaining))
            {
                return GetHandler(remaining);
            }
            else
            {
                return null;
            }
        }

        /// <summary>
        /// Compares and returns api handler with specified <paramref name="path"/>.
        /// </summary>
        /// <exception cref="ArgumentException"></exception>
        private static IAPI GetHandler(PathString path)
        {
            if (path.StartsWithSegments("/NSUDA"))
            {
                return new NSUDAAPI();
            }
            else
            {
                throw new ArgumentException("Handlers with this path is not exist, "
                    + $"path: {path}");
            }
        }
    }
}