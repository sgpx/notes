# Use the official Node.js image as base
FROM node:20

# Set the working directory in the container
WORKDIR /app


# Install dependencies
RUN yarn init --yes
RUN yarn add pg
COPY ./index.js ./app.js
# Expose port 3000 to the outside world
EXPOSE 3000

# Command to run the Node.js application
CMD ["node", "app.js"]
