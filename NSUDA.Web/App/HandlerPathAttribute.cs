namespace NSUDA.Handler
{
    using System;

    /// <summary>
    /// Specifies that method can handle the request and processing path.
    /// </summary>
    [AttributeUsage(AttributeTargets.Method)]
    internal class HandlerPathAttribute : Attribute
    {
        /// <summary>
        /// Processing path.
        /// </summary>
        internal string path { get; set; }
        internal HandlerPathAttribute(string path)
        {
            this.path = path;
        }
    }
}
