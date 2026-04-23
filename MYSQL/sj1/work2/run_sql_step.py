import subprocess
import sys
import re

# MySQL connection settings
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "123456"

def split_sql_statements(content):
    """Split SQL content into individual statements."""
    # Remove comments (lines starting with --)
    lines = content.split('\n')
    cleaned_lines = []
    for line in lines:
        stripped = line.strip()
        if not stripped.startswith('--') and stripped:
            cleaned_lines.append(line)

    cleaned_content = '\n'.join(cleaned_lines)

    # Split by semicolon followed by newline or end
    statements = []
    for stmt in cleaned_content.split(';'):
        stmt = stmt.strip()
        if stmt:
            # Add semicolon back for execution
            statements.append(stmt)

    return statements

def run_sql_step_by_step(sql_file):
    """Execute SQL statements one by one with pause between each."""

    with open(sql_file, 'r', encoding='utf-8') as f:
        content = f.read()

    statements = split_sql_statements(content)

    print(f"共 {len(statements)} 条SQL语句")
    print("=" * 60)
    print("每条执行后会暂停，按回车继续，按 q 退出")
    print("=" * 60)

    for i, stmt in enumerate(statements, 1):
        print(f"\n【第 {i}/{len(statements)} 条】")
        print("-" * 40)
        print("SQL:")
        print(stmt[:200] + "..." if len(stmt) > 200 else stmt)
        print("-" * 40)

        # Build mysql command
        cmd = [
            "mysql",
            "-h", MYSQL_HOST,
            "-u", MYSQL_USER,
            f"-p{MYSQL_PASS}",
            "-e", stmt + ";"
        ]

        # Execute
        try:
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                encoding='utf-8'
            )

            # Show output
            if result.stdout:
                print("结果:")
                print(result.stdout)
            if result.stderr and "Warning" not in result.stderr:
                print(f"[错误] {result.stderr}")
            elif result.stderr:
                # Just show warning briefly
                print(f"[警告] {result.stderr.strip()}")

        except Exception as e:
            print(f"[执行失败] {e}")

        # Wait for user
        user_input = input("\n>>> 按回车继续，按 q 退出: ")
        if user_input.lower() == 'q':
            print("已退出")
            break

    print("\n执行完毕")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python run_sql_step.py <sql文件>")
        sys.exit(1)

    sql_file = sys.argv[1]
    run_sql_step_by_step(sql_file)