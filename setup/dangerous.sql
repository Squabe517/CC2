DO $$ DECLARE
    r RECORD;
BEGIN
    -- Disable referential integrity checks
    PERFORM 'SET session_replication_role = replica';

    -- Drop all tables
    FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = current_schema()) LOOP
        EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    END LOOP;

    -- Re-enable referential integrity checks
    PERFORM 'SET session_replication_role = DEFAULT';
END $$;
