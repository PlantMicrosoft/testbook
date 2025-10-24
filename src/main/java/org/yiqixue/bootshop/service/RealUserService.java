package org.yiqixue.bootshop.service;

import jakarta.validation.Valid;
import org.yiqixue.bootshop.dto.RealUserRegistrationDTO;
import org.yiqixue.bootshop.dto.RealUserResponseDTO;
import org.yiqixue.bootshop.dto.RealUserUpdateDTO;
import org.yiqixue.bootshop.entity.RealUser;
import org.yiqixue.bootshop.mapper.RealUserMapper;
import org.yiqixue.bootshop.repository.RealUserRepository;
import org.springframework.beans.factory.annotation.Autowired;
//import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

/**
 * 用户服务类
 * 处理用户相关的业务逻辑
 */
@Service
@Transactional
public class RealUserService {

    @Autowired
    private RealUserRepository userRepository;

//    @Autowired
//    private PasswordEncoder passwordEncoder;

    @Autowired
    private RealUserMapper userMapper;

    /**
     * 注册用户 - 接收DTO，返回DTO
     */
    public RealUserResponseDTO registerUser(@Valid RealUserRegistrationDTO dto) {
        // 业务验证
        if (userRepository.existsByUsername(dto.getUsername())) {
            throw new RuntimeException("用户名已存在");
        }
        if (userRepository.existsByEmail(dto.getEmail())) {
            throw new RuntimeException("邮箱已被注册");
        }
        if (userRepository.existsByPhone(dto.getPhone())) {
            throw new RuntimeException("手机号码已被注册");
        }

        // 验证密码确认
        if (!dto.getPassword().equals(dto.getConfirmPassword())) {
            throw new RuntimeException("两次输入的密码不一致");
        }

        // DTO转Entity
        RealUser user = userMapper.toEntity(dto);

//        // 加密密码
//        user.setPassword(passwordEncoder.encode(user.getPassword()));
          user.setPassword(user.getPassword());

        // 保存
        RealUser savedUser = userRepository.save(user);

        // Entity转响应DTO返回
        return userMapper.toResponseDTO(savedUser);
    }

    /**
     * 更新用户信息
     */
    public RealUserResponseDTO updateUser(RealUserUpdateDTO dto) {
        RealUser user = userRepository.findById(dto.getId())
                .orElseThrow(() -> new RuntimeException("用户不存在"));

        // 如果要更新密码，需要加密
        if (dto.getPassword() != null && !dto.getPassword().isEmpty()) {
//            dto.setPassword(passwordEncoder.encode(dto.getPassword()));
            dto.setPassword(dto.getPassword());
        }

        // 应用更新
        userMapper.updateEntity(dto, user);

        // 保存并返回
        RealUser updatedUser = userRepository.save(user);
        return userMapper.toResponseDTO(updatedUser);
    }

    /**
     * 获取所有用户 - 返回DTO列表
     */
    public List<RealUserResponseDTO> findAllUsers() {
        return userRepository.findAll().stream()
                .map(userMapper::toResponseDTO)
                .collect(Collectors.toList());
    }

    /**
     * 根据ID查找用户
     */
    public Optional<RealUserResponseDTO> findById(Integer id) {
        RealUser user = userRepository.findById(id)
                .orElseThrow(() -> new RuntimeException("用户不存在"));
        return Optional.ofNullable(userMapper.toResponseDTO(user));
    }

    /**
     * 根据用户名查找用户
     */
    public Optional<RealUser> findByUsername(String username) {
        return userRepository.findByUsername(username);
    }

    /**
     * 根据ID查找用户
     */
//    public Optional<RealUser> findById(Integer id) {
//        return userRepository.findById(id);
//    }

    /**
     * 获取所有用户
     */
//    public List<RealUser> findAllUsers() {
//        return userRepository.findAll();
//    }

    /**
     * 更新用户信息
     */
    public RealUser updateUser(RealUser user) {
        return userRepository.save(user);
    }

    /**
     * 删除用户
     */
    public void deleteUser(Integer id) {
        userRepository.deleteById(id);
    }

    /**
     * 检查用户名是否可用
     */
    public boolean isUsernameAvailable(String username) {
        return !userRepository.existsByUsername(username);
    }

    /**
     * 检查邮箱是否可用
     */
    public boolean isEmailAvailable(String email) {
        return !userRepository.existsByEmail(email);
    }

    /**
     * 检查手机号码是否可用
     */
    public boolean isPhoneAvailable(String phone) {
        return !userRepository.existsByPhone(phone);
    }
}