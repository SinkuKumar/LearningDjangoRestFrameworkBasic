### How to Run the Script with Command Line Arguments

You can specify the number of blogs you want to create using the `--num-blogs` argument. If you don't specify it, it will default to 20.

#### Here are the examples:

- To create the default 20 blogs:
  ```bash
  python manage.py generate_fake_data
  ```

- To create a specific number of blogs, say 10:
  ```bash
  python manage.py generate_fake_data --num-blogs 10
  ```

This way, you can easily control how many blogs you want to generate from the command line!

To create management commands for generating fake data for users, likes, dislikes, and comments, you can follow a similar approach to the blog generation command. Below is a structure where each command can accept arguments to specify how many entries to create.


### Running the Commands

You can run each command individually from the command line:

- To generate users:
  ```bash
  python manage.py generate_users --num-users 10
  ```

- To generate blogs:
  ```bash
  python manage.py generate_blogs --num-blogs 20
  ```

- To generate comments:
  ```bash
  python manage.py generate_comments --num-comments 50
  ```

- To generate likes:
  ```bash
  python manage.py generate_likes --num-likes 100
  ```

- To generate dislikes:
  ```bash
  python manage.py generate_dislikes --num-dislikes 50
  ```

Certainly! You can create a single management command that will generate users, blogs, comments, likes, and dislikes in one go. Here’s how you can do it:

### How to Run the Combined Command

You can run this command from the command line, specifying the number of entries you want for each model.

```bash
python manage.py generate_data --num-users 10 --num-blogs 20 --num-comments 50 --num-likes 100 --num-dislikes 50
```

If you do not specify the arguments, it will use the default values:

```bash
python manage.py generate_data
```

### Explanation

- The command accepts arguments for the number of users, blogs, comments, likes, and dislikes.
- It creates users first, then generates blogs using those users, and subsequently generates comments, likes, and dislikes associated with the created blogs and users.

This single command simplifies data generation for testing and development!