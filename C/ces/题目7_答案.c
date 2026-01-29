#include <stdio.h>
#include <string.h>

#define MAX_STUDENTS 100

struct Student {
    char name[20];
    char id[15];
    double scores[3];
    double average;
};

struct Student students[MAX_STUDENTS];
int studentCount = 0;

// 计算平均分
void CalculateAverage(struct Student *s) {
    s->average = (s->scores[0] + s->scores[1] + s->scores[2]) / 3.0;
}

// 添加学生
void AddStudent() {
    if (studentCount >= MAX_STUDENTS) {
        printf("学生数量已达上限！\n");
        return;
    }
    
    printf("请输入学生姓名：");
    scanf("%s", students[studentCount].name);
    printf("请输入学号：");
    scanf("%s", students[studentCount].id);
    printf("请输入三门课成绩：");
    for (int i = 0; i < 3; i++) {
        scanf("%lf", &students[studentCount].scores[i]);
    }
    
    CalculateAverage(&students[studentCount]);
    studentCount++;
    printf("添加成功！\n");
}

// 显示所有学生
void DisplayAll() {
    if (studentCount == 0) {
        printf("暂无学生信息！\n");
        return;
    }
    
    printf("\n%-15s %-12s %-8s %-8s %-8s %-8s\n", 
           "姓名", "学号", "成绩1", "成绩2", "成绩3", "平均分");
    printf("----------------------------------------------------------------\n");
    
    for (int i = 0; i < studentCount; i++) {
        printf("%-15s %-12s %-8.2f %-8.2f %-8.2f %-8.2f\n",
               students[i].name, students[i].id,
               students[i].scores[0], students[i].scores[1], 
               students[i].scores[2], students[i].average);
    }
    printf("\n");
}

// 按平均分排序
void SortByAverage() {
    for (int i = 0; i < studentCount - 1; i++) {
        for (int j = 0; j < studentCount - 1 - i; j++) {
            if (students[j].average < students[j+1].average) {
                struct Student temp = students[j];
                students[j] = students[j+1];
                students[j+1] = temp;
            }
        }
    }
    printf("排序完成！\n");
}

// 查找学生
void SearchStudent() {
    char id[15];
    printf("请输入要查找的学号：");
    scanf("%s", id);
    
    for (int i = 0; i < studentCount; i++) {
        if (strcmp(students[i].id, id) == 0) {
            printf("\n找到学生：\n");
            printf("姓名：%s\n", students[i].name);
            printf("学号：%s\n", students[i].id);
            printf("成绩：%.2f %.2f %.2f\n", 
                   students[i].scores[0], students[i].scores[1], students[i].scores[2]);
            printf("平均分：%.2f\n\n", students[i].average);
            return;
        }
    }
    printf("未找到该学生！\n");
}

// 保存到文件
void SaveToFile() {
    FILE *fp = fopen("students.dat", "wb");
    if (fp == NULL) {
        printf("文件打开失败！\n");
        return;
    }
    
    fwrite(&studentCount, sizeof(int), 1, fp);
    fwrite(students, sizeof(struct Student), studentCount, fp);
    fclose(fp);
    printf("保存成功！\n");
}

// 从文件读取
void LoadFromFile() {
    FILE *fp = fopen("students.dat", "rb");
    if (fp == NULL) {
        printf("文件不存在或打开失败！\n");
        return;
    }
    
    fread(&studentCount, sizeof(int), 1, fp);
    fread(students, sizeof(struct Student), studentCount, fp);
    fclose(fp);
    printf("读取成功！共%d名学生\n", studentCount);
}

int main() {
    int choice;
    
    while (1) {
        printf("\n========== 学生信息管理系统 ==========\n");
        printf("1. 添加学生\n");
        printf("2. 显示所有学生\n");
        printf("3. 按平均分排序\n");
        printf("4. 查找学生\n");
        printf("5. 保存到文件\n");
        printf("6. 从文件读取\n");
        printf("0. 退出\n");
        printf("=====================================\n");
        printf("请选择：");
        
        scanf("%d", &choice);
        
        switch (choice) {
            case 1:
                AddStudent();
                break;
            case 2:
                DisplayAll();
                break;
            case 3:
                SortByAverage();
                break;
            case 4:
                SearchStudent();
                break;
            case 5:
                SaveToFile();
                break;
            case 6:
                LoadFromFile();
                break;
            case 0:
                printf("感谢使用！\n");
                return 0;
            default:
                printf("无效选择！\n");
        }
    }
    
    return 0;
}
