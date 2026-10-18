UPDATE wp_users SET user_pass = MD5('new_password') WHERE user_login = 'your_admin_username';
