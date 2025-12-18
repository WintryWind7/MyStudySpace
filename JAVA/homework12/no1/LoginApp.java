package homework12.no1;

import javax.swing.*;
import java.awt.*;

public class LoginApp extends JFrame {
    private final JTextField usernameField = new JTextField(12);
    private final JPasswordField passwordField = new JPasswordField(12);

    public LoginApp() {
        setTitle("学生管理系统");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        initUI();
        pack();
        setLocationRelativeTo(null);
    }

    private void initUI() {
        setLayout(new BorderLayout(0, 12));

        JPanel formPanel = new JPanel(new GridBagLayout());
        GridBagConstraints gbc = new GridBagConstraints();
        gbc.insets = new Insets(8, 15, 8, 15);
        gbc.anchor = GridBagConstraints.WEST;
        gbc.fill = GridBagConstraints.HORIZONTAL;

        gbc.gridx = 0;
        gbc.gridy = 0;
        formPanel.add(new JLabel("登录名"), gbc);

        gbc.gridx = 1;
        formPanel.add(usernameField, gbc);

        gbc.gridx = 0;
        gbc.gridy = 1;
        formPanel.add(new JLabel("密  码"), gbc);

        gbc.gridx = 1;
        formPanel.add(passwordField, gbc);

        JPanel buttonPanel = new JPanel(new FlowLayout(FlowLayout.CENTER, 20, 5));

        JButton loginButton = new JButton("登录");
        loginButton.addActionListener(e -> onLogin());
        buttonPanel.add(loginButton);

        JButton cancelButton = new JButton("取消");
        cancelButton.addActionListener(e -> onCancel());
        buttonPanel.add(cancelButton);

        add(formPanel, BorderLayout.CENTER);
        add(buttonPanel, BorderLayout.SOUTH);
    }

    private void onLogin() {
        String username = usernameField.getText();
        String password = String.valueOf(passwordField.getPassword());

        if ("why".equals(username) && "45".equals(password)) {
            JOptionPane.showMessageDialog(this, "输入成功", "提示", JOptionPane.INFORMATION_MESSAGE);
        } else {
            JOptionPane.showMessageDialog(this, "登录失败", "提示", JOptionPane.ERROR_MESSAGE);
        }
    }

    private void onCancel() {
        usernameField.setText("");
        passwordField.setText("");
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new LoginApp().setVisible(true));
    }
}
