# Resume Application

If you want to play around with this application you will need to have `docker` and `docker-compose` installed.  Once those requirements are met simply follow these directions:

```
git clone git@github.com:youssefmkb/ResumeApplication.git .
docker-compose up -d --build
```

Then simply navigate to `localhost:8123` to start building your resume.  
You can monitor the output from the Django development server using this command: `docker logs -f resume_app`.
