CREATE DEFINER=`root`@`localhost` TRIGGER `after_user_insert` AFTER INSERT ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, new_name, new_email, changed_by)
    VALUES (NEW.id, 'INS', NEW.name, NEW.email, current_user());
END


CREATE DEFINER=`root`@`localhost` TRIGGER `after_user_update` AFTER UPDATE ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type,
        old_name, old_email,
        new_name, new_email,
        changed_by
    )
    VALUES (
        OLD.id, 'UPDATE',
        OLD.name, OLD.email,
        NEW.name, NEW.email,
        CURRENT_USER()
    );
END



CREATE DEFINER=`root`@`localhost` TRIGGER `after_user_delete` AFTER DELETE ON `users` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, old_name, old_email, changed_by)
    VALUES (OLD.id, 'DELETE', OLD.name, OLD.email, current_user());
END



CREATE DEFINER=`root`@`localhost` TRIGGER `after_admin_insert` AFTER INSERT ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (user_id, action_type, new_name, new_email, changed_by)
    VALUES (NEW.id, 'INSERT', NEW.name, NEW.email, current_user());
END



CREATE DEFINER=`root`@`localhost` TRIGGER `after_admin_update` AFTER UPDATE ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type,
        old_name, old_email,
        new_name, new_email,
        changed_by
    )
    VALUES (
        OLD.id, 'UPDATE',
        OLD.name, OLD.email,
        NEW.name, NEW.email,
        CURRENT_USER()
    );
END



CREATE DEFINER=`root`@`localhost` TRIGGER `after_admin_delete` AFTER DELETE ON `admins` FOR EACH ROW BEGIN
    INSERT INTO user_log (
        user_id, action_type, 
        old_name, old_email, 
        changed_by
    )
    VALUES (
        OLD.id, 'DELETE', 
        OLD.name, OLD.email, 
        CURRENT_USER()
    );
END

