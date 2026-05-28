---
title: Troubleshooting Guide | Developer Documentation
---

## Self-Hosting Documentation Access

This section requires a password to access. Interested in self-hosting? [Contact sales](https://www.llamaindex.ai/contact) to learn more.

Password:

Access Documentation

Self-Hosting Documentation Access Granted Logout

This guide helps you diagnose and resolve common issues when deploying LlamaCloud on Azure. Use this after completing the [Azure Setup Guide](/llamaparse/self_hosting/cloud-specific-guides/azure/setup/index.md) if you encounter problems.

## General Debugging Commands

### Pod Status and Logs

Terminal window

```
# Check all pod status
kubectl get pods -n llamacloud -o wide


# Describe problematic pods
kubectl describe pod <pod-name> -n llamacloud


# Check logs for specific services
kubectl -n llamacloud logs deployment/llamacloud-telemetry
kubectl -n llamacloud logs deployment/llamacloud-parse
kubectl -n llamacloud logs deployment/llamacloud-web
kubectl -n llamacloud logs deployment/llamacloud-worker
kubectl -n llamacloud logs deployment/llamacloud-ocr
kubectl -n llamacloud logs deployment/llamacloud-s3proxy
```

### Service and Secret Status

Terminal window

```
# Check services
kubectl get svc -n llamacloud


# Verify secrets exist
kubectl get secrets -n llamacloud


# Check configmaps
kubectl get configmaps -n llamacloud
```

## Database Connection Issues

### PostgreSQL Connection Problems

**Symptoms:**

- Backend pods failing to start
- Database connection errors in logs
- “connection refused” or “timeout” errors

**Solutions:**

1. **Verify database connection:**

   Terminal window

   ```
   # Test connection from AKS
   kubectl run -it --rm debug --image=postgres:15 --restart=Never -- psql "postgresql://username:password@server.postgres.database.azure.com:5432/llamacloud"
   ```

2. **Check secret values:**

   Terminal window

   ```
   kubectl get secret postgresql-secret -o yaml
   # Verify DATABASE_HOST, DATABASE_USER, etc. are correct
   ```

3. **Common fixes:**

   - Add AKS subnet to PostgreSQL firewall rules
   - Verify SSL is enabled (required by Azure Database for PostgreSQL)
   - Check database name exists
   - Verify user permissions

### Redis Connection Issues

**Symptoms:**

- “Redis connection failed” in backend logs
- Authentication errors
- SSL/TLS errors

**Solutions:**

1. **Test Redis connectivity:**

   Terminal window

   ```
   kubectl run -it --rm redis-test --image=redis:7 --restart=Never -- redis-cli -h your-redis.redis.cache.windows.net -p 6380 --tls -a your-access-key ping
   ```

2. **Check SSL configuration:**

   - Azure Redis requires SSL on port 6380
   - Verify `REDIS_SCHEME: "rediss"` in secret
   - Ensure `REDIS_PORT: "6380"` for SSL

3. **Verify access key:**

   - Copy primary access key exactly from Azure Portal
   - No extra spaces or characters

## Service Bus Connection Issues

**Symptoms:**

- Jobs worker fails to start
- “Service Bus connection failed” errors
- Queue creation errors

**Solutions:**

1. **Verify connection string format:**

   ```
   Endpoint=sb://namespace.servicebus.windows.net/;SharedAccessKeyName=policy;SharedAccessKey=key
   ```

2. **Check permissions:**

   - Shared access policy must have **Manage**, **Send**, and **Listen** rights
   - Standard tier or higher required (Basic not supported)

3. **Test connectivity:**

   Terminal window

   ```
   # From Azure Portal, test connection using Service Bus Explorer
   ```

## Cosmos DB (MongoDB) Issues

**Symptoms:**

- MongoDB connection errors
- “SSL/TLS handshake failed”
- “API type not supported”

**Solutions:**

1. **Verify MongoDB API:**

   - Must use MongoDB API, not SQL API
   - Check API type in Cosmos DB Overview

2. **Check connection string:**

   ```
   mongodb://account:key@account.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@account@
   ```

3. **SSL requirements:**

   - SSL is required for Cosmos DB
   - Connection string includes `ssl=true`

## Storage Issues

### Blob Storage / S3Proxy Problems

**Symptoms:**

- File upload failures
- S3Proxy pod crashlooping
- “Access denied” errors

**Solutions:**

1. **Check s3proxy logs:**

   Terminal window

   ```
   kubectl logs deployment/llamacloud-s3proxy -n llamacloud
   ```

2. **Verify container names:**

   - All required containers must exist
   - Names are case-sensitive
   - Check containers in Azure Portal

3. **Required containers:**

   ```
   llama-platform-parsed-documents
   llama-platform-etl
   llama-platform-external-components
   llama-platform-file-parsing
   llama-platform-raw-files
   llama-cloud-parse-output
   llama-platform-file-screenshots
   llama-platform-extract-output
   ```

4. **Check s3proxy configuration:**

   - Review [s3proxy configuration docs](https://github.com/gaul/s3proxy)

## Azure OpenAI Issues

### Model Deployment Problems

**Symptoms:**

- “Model not found” errors
- “Deployment not found” errors
- API version errors

**Solutions:**

1. **Check job service logs:**

   Terminal window

   ```
   kubectl logs deployment/llamacloud-worker -n llamacloud
   ```

   We run LLM integration validators on pod startup. You can find useful error logs for LLM integrations.

2. **Verify deployment names:**

   - Use deployment name, not model name
   - Check in Azure Portal → Model deployments

3. **Check quotas:**

   - Ensure sufficient TPM quota allocated
   - Verify deployment is not paused

4. **API version:**

   - Use supported version: `2024-12-01-preview`
   - Check Azure OpenAI documentation for latest

5. **Test direct access:**

   Terminal window

   ```
   curl -H "api-key: YOUR_KEY" \
        "https://YOUR_RESOURCE.openai.azure.com/openai/deployments/YOUR_DEPLOYMENT/completions?api-version=2024-12-01-preview"
   ```

## Authentication Issues

### Microsoft Entra ID OIDC Problems

**Symptoms:**

- Authentication redirects fail
- “Invalid client” errors
- OIDC discovery errors

**Solutions:**

1. **Verify app registration:**

   - Check client ID is correct
   - Verify redirect URIs are configured
   - Ensure client secret is valid (not expired)

2. **Check discovery URL:**

   ```
   https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
   ```

3. **Test OIDC endpoint:**

   Terminal window

   ```
   curl https://login.microsoftonline.com/{tenant-id}/v2.0/.well-known/openid-configuration
   ```

## Pod-Specific Issues

### Backend Pod Issues

**Common problems:**

- Environment variable errors
- Secret mounting failures
- Database migration failures

**Debug steps:**

Terminal window

```
kubectl logs deployment/llamacloud --tail=100 -n llamacloud
kubectl describe deployment llamacloud -n llamacloud
kubectl get events --sort-by='.lastTimestamp' -n llamacloud
```

### Frontend Pod Issues

**Common problems:**

- Build failures
- Configuration errors
- Ingress connectivity

**Debug steps:**

Terminal window

```
kubectl -n llamacloud logs deployment/llamacloud-web --tail=100
kubectl -n llamacloud port-forward svc/llamacloud-web 3000:80
```

### Jobs Worker Issues

**Common problems:**

- Queue connectivity
- Job processing failures
- Memory/CPU limits

**Debug steps:**

Terminal window

```
kubectl -n llamacloud logs deployment/llamacloud-worker --tail=100
kubectl -n llamacloud top pod -l app=llamacloud-worker
```

## Network and Security Issues

### AKS Networking Problems

**Symptoms:**

- Pods cannot reach Azure services
- DNS resolution failures
- Intermittent connectivity

**Solutions:**

1. **Check network security groups:**

   - Verify outbound rules allow Azure service connections
   - Check subnet NSG rules

2. **Verify DNS:**

   Terminal window

   ```
   kubectl run -it --rm nslookup --image=busybox --restart=Never -- nslookup your-postgres.postgres.database.azure.com
   ```

3. **Test private endpoints:**

   - If using private endpoints, verify routing
   - Check private DNS zones

### Ingress Issues

**Symptoms:**

- Cannot access LlamaCloud UI externally
- SSL certificate errors
- Load balancer failures

**Solutions:**

1. **Check ingress controller:**

   Terminal window

   ```
   kubectl get ingress
   kubectl logs -n ingress-nginx deployment/nginx-ingress-controller
   ```

2. **Verify DNS configuration:**

   - Domain points to load balancer IP
   - SSL certificates are valid

3. **Test load balancer:**

   Terminal window

   ```
   kubectl get svc -n ingress-nginx
   ```

## Performance Issues

### Slow Performance

**Common causes:**

- Insufficient resources
- Database performance issues
- Network latency

**Solutions:**

1. **Check resource usage:**

   Terminal window

   ```
   kubectl top pods
   kubectl top nodes
   ```

2. **Scale resources:**

   Terminal window

   ```
   kubectl scale deployment llamacloud --replicas=3 -n llamacloud
   ```

3. **Optimize Azure services:**

   - Increase PostgreSQL compute tier
   - Use Premium Redis tier
   - Enable auto-scaling for Cosmos DB

### Memory/CPU Issues

**Symptoms:**

- Pod restarts
- OOMKilled events
- High CPU usage

**Solutions:**

1. **Check resource limits:**

   Terminal window

   ```
   kubectl describe pod <pod-name> -n llamacloud
   ```

2. **Increase limits in values.yaml:**

   ```
   backend:
     resources:
       limits:
         memory: 4Gi
         cpu: 2
   ```

## Error Code Reference

### Common HTTP Errors

- **500 Internal Server Error**: Check backend logs, database connectivity
- **502 Bad Gateway**: Check if backend pods are running
- **503 Service Unavailable**: Check service health, scaling issues
- **401 Unauthorized**: OIDC configuration issues
- **403 Forbidden**: Azure service permission issues

### Common Database Errors

- **Connection refused**: Firewall or network issues
- **Authentication failed**: Wrong credentials
- **SSL required**: Missing SSL configuration
- **Database does not exist**: Database name mismatch

## Getting Help

### Collect Diagnostic Information

Before contacting support, gather:

Terminal window

```
# Basic cluster info
kubectl -n llamacloud get pods -o wide
kubectl -n llamacloud get svc
kubectl -n llamacloud get secrets
kubectl -n llamacloud get configmaps


# Logs from all services
kubectl -n llamacloud logs deployment/llamacloud              > llamacloud.log
kubectl -n llamacloud logs deployment/llamacloud-layout       > llamacloud-layout.log
kubectl -n llamacloud logs deployment/llamacloud-ocr          > llamacloud-ocr.log
kubectl -n llamacloud logs deployment/llamacloud-operator     > llamacloud-operator.log
kubectl -n llamacloud logs deployment/llamacloud-parse        > llamacloud-parse.log
kubectl -n llamacloud logs deployment/llamacloud-telemetry    > llamacloud-telemetry.log
kubectl -n llamacloud logs deployment/llamacloud-web          > llamacloud-web.log
kubectl -n llamacloud logs deployment/llamacloud-worker       > llamacloud-worker.log
kubectl -n llamacloud logs deployment/llamacloud-s3proxy      > llamacloud-s3proxy.log


# Cluster events
kubectl get events --sort-by='.lastTimestamp' -n llamacloud


# Resource usage
kubectl top pods
kubectl top nodes
```

### Contact Support

- **LlamaCloud Support**: <support@llamaindex.ai>
- **Include**: Deployment configuration, error logs, Azure resource details
- **Avoid**: Sharing secrets, credentials, or sensitive data
