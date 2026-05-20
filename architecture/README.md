# Architecture Diagram

   [To be added: S3 → Lambda → RDS → Dashboard]

   ## Data Flow
   1. User uploads LiDAR file to S3 bucket
   2. S3 triggers Lambda function
   3. Lambda processes with PDAL
   4. Results stored in PostGIS (RDS)
   5. Dashboard reads from database
