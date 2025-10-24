package org.yiqixue.bootshop.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import java.time.LocalDate;
import java.util.Set;

/**
 * 用户实体类
 * 对应数据库中的 user 表
 */
@Entity
@Table(name = "users")
@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class RealUser {


    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(nullable = false, unique = true, length = 20)
    private String username;

    @Column(nullable = false)
    private String password;

    @Column(nullable = false, unique = true)
    private String email;

    @Column(length = 20)
    private String phone;

    @Column(name = "real_name", length = 50)
    private String realName;

    @Column(nullable = false)
    private String gender;

    @Column(name = "birth_date")
    private LocalDate birthDate;

    private Integer age;

    @Column(length = 50)
    private String country;

    @Column(length = 50)
    private String city;

    @Column(length = 500)
    private String bio;

    @Column(length = 200)
    private String hobbies;

    @Column(name = "newsletter_subscription")
    private Boolean newsletterSubscription;

    @Column(name = "terms_accepted")
    private Boolean termsAccepted;

    @Column(name = "register_date")
    private LocalDate registerDate;

    @PrePersist
    protected void onCreate() {
        if (registerDate == null) {
            registerDate = LocalDate.now();
        }
        if (newsletterSubscription == null) {
            newsletterSubscription = false;
        }
        if (termsAccepted == null) {
            termsAccepted = false;
        }
    }
}
