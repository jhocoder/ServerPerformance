Server Efficiency Evaluation: Benchmarking Apache, Nginx, Node.js, and PHP 🧑‍💻

This week, I performed a comparative performance analysis of several web servers on a Linux virtual machine using Apache Benchmark (AB). The primary objective was to measure the efficiency of different servers under load conditions. The servers tested include:

    Apache HTTP Server
    Nginx
    Apache + PHP-FPM
    Nginx + PHP-FPM
    Node.js

A self-created static webpage and a PHP-based dynamic page were served across these environments to simulate real-world scenarios.
Methodology
Tools and Libraries Utilized:

    subprocess (Python): For automating server benchmarking tasks and capturing raw output.
    pandas: To process benchmark data, structure it in a DataFrame, and export it to Excel for further analysis.
    matplotlib: For visualizing benchmark metrics, such as throughput and latency, in graph form.

Benchmarking Parameters:

    Tool: Apache Benchmark (ab)
    Tests Conducted:
        3 iterations for each configuration.
        500 HTTP requests per test with 10 concurrent connections.
    Metrics Extracted:
        Requests per second (req/s)
        Time per request (ms/req)
        Transfer rate (kB/s)

Results
Observations by Server Type:

    Node.js:
        Delivered the highest throughput (requests/sec).
        Achieved the best transfer rate due to its event-driven, non-blocking I/O architecture (powered by libuv).
        Showcased exceptional performance under concurrent workloads.

    Nginx:
        Demonstrated excellent concurrency management, slightly trailing Node.js in throughput.
        Benefited from its asynchronous event-driven model.

    Apache (Standalone):
        Consistently reliable under load, utilizing its prefork and worker modules.
        Marginally less efficient than Nginx in handling concurrency.

    Apache + PHP-FPM and Nginx + PHP-FPM:
        Experienced higher request times due to the overhead of executing PHP scripts via FastCGI Process Manager (PHP-FPM).
        Suitable for dynamic content delivery, albeit with lower raw performance compared to Node.js or static-serving Nginx.

Conclusion

    Node.js: Best suited for applications demanding high performance and concurrency, such as real-time systems or APIs.
    Nginx: Ideal for serving static content or acting as a reverse proxy with minimal latency.
    Apache: Versatile and robust, particularly for legacy applications.
    Apache + PHP-FPM / Nginx + PHP-FPM: Recommended for PHP-based dynamic applications, balancing functionality and performance.

Takeaways

This benchmarking exercise enabled me to:

    Automate performance testing pipelines using Python.
    Gain deeper insights into server architectures and their impact on load handling.
    Enhance data analysis and visualization skills using pandas and matplotlib.
